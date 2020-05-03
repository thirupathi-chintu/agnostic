module "dev" {
    source "./env"

    env = "dev"
    aws_ssh_keyname = "dev_ssh"
}

module "stage" {
    source "./env"

    env = "stage"
    aws_ssh_keyname = "stage_ssh"
}
