import os
import subprocess
import sys
import yaml

lang = "cs"

def load_localization(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        localization = yaml.safe_load(file)
    return localization

def generate_ssh_key(alias, localization):
    output_file = os.path.expanduser(f'~/.ssh/{alias}_deploy_key')
    subprocess.run(['ssh-keygen', '-t', 'rsa', '-b', '4096', '-C', f'{alias} Key', '-f', output_file])
    print(f'{localization[lang]["ssh_key_pair_1"]} "{alias}" {localization[lang]["ssh_key_pair_2"]} {output_file}.')
    public_key_file = f'{output_file}.pub'
    with open(public_key_file, 'r') as pubkey_file:
        public_key = pubkey_file.read().strip()
    return public_key

def configure_ssh_config(alias, localization):
    identity_file = os.path.expanduser(f'~/.ssh/{alias}_deploy_key')
    ssh_config_entry = f'\nHost github.com-{alias}\n' \
                       f'        Hostname github.com\n' \
                       f'        IdentityFile={identity_file}'
    with open(os.path.expanduser('~/.ssh/config'), 'a') as config_file:
        config_file.write(ssh_config_entry)
    print(f'{localization[lang]["config_gen_1"]} "{alias}" {localization[lang]["config_gen_2"]}.')

# git clone alias:Trnass/maturita.trnass.cz.git    
# git@github.com-test:Trnass/sshkeypair_generator.git

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'{localization[lang]["usage"]}')
    else:
        alias = sys.argv[1]
        localization = load_localization('localization.yaml')
        public_key = generate_ssh_key(alias, localization)
        configure_ssh_config(alias, localization)
        print(f'\n{localization[lang]["public_key"]}\n{public_key}\n')
        print(f'\n{localization[lang]["todo_git_init"]}\ngit init\n')
        print(f'\n{localization[lang]["todo_git_clone"]}\ngit clone git@github.com-{alias}/{localization[lang]["author_link"]}/{localization[lang]["nazev_repozitare"]}.git\n')
