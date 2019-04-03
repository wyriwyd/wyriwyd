#!/bin/bash
read -p "Output file name (.md): " outfile
rm -f "$outfile"
echo -e "Start typing your commands. When done, press enter.
File $outfile containing the session will be genarated."
while read -p "$ " command && test -n "$command" ; do
    output="$(script -c "$command" -q --)"
    echo -e "$output\n"
    if [ -n "$output" ]; then
        echo -e "\`\`\`bash\n${command}\n\`\`\`\n\n\`\`\`\n$output\n\`\`\`\n" >> "$outfile"
    else
        echo -e "\`\`\`bash\n${command}\n\`\`\`\n" >> "$outfile"
    fi
done
