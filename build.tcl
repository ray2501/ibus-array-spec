#!/usr/bin/tclsh

set arch "x86_64"
set base "ibus-array-0.2.3"

set var2 [list git clone https://github.com/lexical/ibus-array.git $base]
exec >@stdout 2>@stderr {*}$var2

cd $base

set var2 [list git checkout f93e181e78e2861fceb9c2baa14dc67c8506963c]
exec >@stdout 2>@stderr {*}$var2

set var2 [list git reset --hard]
exec >@stdout 2>@stderr {*}$var2

file delete -force .git

cd ..

set var2 [list tar czvf ${base}.tar.gz $base]
exec >@stdout 2>@stderr {*}$var2

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb ibus-array.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete $base.tar.gz
