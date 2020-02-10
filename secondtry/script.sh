#!/bin/bash
ENV_NAMES=('$HOME' '$PWD' '$QWERTY')
ENV_VALUES=(1 2 3)

env_values_gain () {
}

env_update () {
    echo ${ENV_NAMES[i]}
    echo ${ENV_VALUES[i]}
	sed -i 's|'"${ENV_NAMES[i]}"'|'"${ENV_VALUES[i]}"'|g' playbook.yml
}

main (){
    for i in ${!ENV_NAMES[@]}; do
        env_update
    done
}

main
