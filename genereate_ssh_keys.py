import os
import subprocess
import sys

def generate_ssh_key(alias):
    output_file = os.path.expanduser(f'~/.ssh/{alias}_deploy_key')
    subprocess.run(['ssh-keygen', '-t', 'rsa', '-b', '4096', '-C', f'{alias} Key', '-f', output_file])
    print(f'SSH key pair pro alias "{alias}" úspěšně vygenerován do {output_file}.')
    public_key_file = f'{output_file}.pub'
    with open(public_key_file, 'r') as pubkey_file:
        public_key = pubkey_file.read().strip()
    return public_key

def configure_ssh_config(alias):
    identity_file = os.path.expanduser(f'~/.ssh/{alias}_deploy_key')
    ssh_config_entry = f'\nHost github.com-{alias}\n' \
                       f'        Hostname github.com\n' \
                       f'        IdentityFile={identity_file}'
    with open(os.path.expanduser('~/.ssh/config'), 'a') as config_file:
        config_file.write(ssh_config_entry)
    print(f'SSH config pro alias "{alias}" úspěšně přidán.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_ssh_keys.py <alias>")
    else:
        alias = sys.argv[1]
        public_key = generate_ssh_key(alias)
        configure_ssh_config(alias)
        print(f'Public key to add to GitHub:\n{public_key}')
