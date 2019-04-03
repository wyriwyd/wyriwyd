#!/bin/bash
read -p "Output file name (.md): " outfile
rm -f "$outfile"
echo -e "Start typing your commands. When done, press enter.
File $outfile containing the session will be genarated."
mysys="$(uname -s)"
tmpfile="/tmp/mytemp"
while read -p "$ " command && test -n "$command" ; do
    if [ "$mysys" = "Linux" ]; then
        output="$(script -c "$command" -q --)"
    elif [ "$mysys" = "Darwin" ]; then
        output="$(script "$tmpfile" "$command" -q ; cat "$tmpfile")"
        rm "$tmpfile"
    else
        echo "Unknown system"
        return 1
    fi
    echo -e "$output\n"
    if [ -n "$output" ]; then
        echo -e "\`\`\`bash\n${command}\n\`\`\`\n\n\`\`\`\n$output\n\`\`\`\n" >> "$outfile"
    else
        echo -e "\`\`\`bash\n${command}\n\`\`\`\n" >> "$outfile"
    fi
done
