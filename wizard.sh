#!/bin/bash
command="ls"
rm -f wizard.out
echo -e "Start typing your commands. When done, press enter.
File wizard.out containing the session will be genarated."
while [ -n "$command" ] ; do
    read -p "$ " command
    #    foo="$(script -c "$command" -q -)"
    foo="$(eval "$command")"
    echo -e "$foo\n"
    echo -e "$ ${command}\n$foo\n" >> wizard.out
done
