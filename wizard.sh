#!/bin/bash
rm -f wizard.out
echo -e "Start typing your commands. When done, press enter.
File wizard.out containing the session will be genarated."
while read -p "$ " command && test -n "$command" ; do
    output="$(script -c "$command" -q -)"
    echo -e "$output\n"
    echo -e "\`\`\`bash\n$ ${command}\n\`\`\`\n\n\`\`\`\n$output\n\`\`\`\n" >> wizard.out
done
rm -- -
