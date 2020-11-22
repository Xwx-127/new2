import yaml


class GetYaml:
    def get_yaml(self):
        with open('token.yaml', 'r', encoding='utf_8') as f:
            res = f.read()
            r = yaml.safe_load(res)
        return r['env']

if __name__ == '__main__':
    print(GetYaml().get_yaml())
