#!/usr/bin/bash

name=$1
lowercase_name=$2
url="$(curl -sI "$3" | grep location | cut -d' ' -f2 | dos2unix)"
version="$(echo ${url} | grep -Eo "${lowercase_name}-[0-9.]+[0-9]" | grep -Eo [0-9.]+)"
rebuild="false"
rebuild_trigger="/var/lib/discord-installer-rebuild-${name}"
arch="$(uname -m)"

if rpm -qi ${name} &> /dev/null && [[ $(rpm -q --queryformat '%{VERSION}' ${name}) = ${version} ]]
then
    if [[ -f ${rebuild_trigger} ]]
    then
        rebuild="true"
    else
        exit 0
    fi
fi

export HOME="/tmp/discord-installer"
[ -d ${HOME} ] && rm -r ${HOME}
mkdir -p ${HOME}
rpmdev-setuptree

cp /usr/share/discord-installer/template.spec ${HOME}/rpmbuild/SPECS/${name}.spec
pushd ${HOME}/rpmbuild/SPECS

sed -i "s,\[name\],${name},"                      ${name}.spec
sed -i "s,\[lowercase_name\],${lowercase_name},"  ${name}.spec
sed -i "s,\[url\],${url},"                        ${name}.spec

rpmdev-bumpspec -n ${version} -c "Update to ${version}" ${name}.spec

spectool -g -C ../SOURCES ${name}.spec
rpmbuild -bb ${name}.spec

if which dnf &> /dev/null
then
    package_manager="dnf"
else
    package_manager="yum"
fi

if ${package_manager} install -y ../RPMS/${arch}/*.rpm || ${package_manager} reinstall -y ../RPMS/${arch}/*.rpm
then
    if ${rebuild}
    then
        message="$1 version ${version} rebuilt"
    else
        message="$1 updated to version ${version}"
    fi
else
    message="$1 could not be updated (${package_manager} exit status: $?)"
fi

popd

if [[ -f ${rebuild_trigger} ]]
then
    rm -f ${rebuild_trigger}
fi

who | while read line
do
    pkexec --user $(echo ${line} | cut -d' ' -f1) notify-send --icon "$2" "${message}"
done

exit 0
