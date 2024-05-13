import yaml


def generate_ans(tasks):
    playbook = []
    ansible_task = {"name": "Install packages "}
    ansible_task["apt"] = ansible_task["name"] + ",".join(
        tasks["server"]["install_packages"]
    )
    playbook.append({"task": "name", "debug": {"msg": ansible_task}})
    ansible_task["name"] = "Exploit files"
    ansible_task["copy"] = {
        "src": tasks["server"]["exploit_files"],
        "dest": "{{server}}",
    }
    playbook.append({"task": "name", "debug": {"msg": ansible_task}})
    ansible_task["name"] = "bad_guys"
    ansible_task["lineinfile"] = {
        "path": "{{server}}",
        "line": "{{item}}",
        "with_items": tasks["bad_guys"],
    }
    return playbook


def main():
    with open("../materials/todo.yml", "r") as file:
        tasks = yaml.safe_load(file)

    ap = generate_ans(tasks)
    with open("../materials/deploy.yml", "w") as file:
        yaml.dump(ap, file)


if __name__ == "__main__":
    main()
