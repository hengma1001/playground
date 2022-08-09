# %%
import yaml
if __name__ == '__main__':
    f = open("conf.yml", 'r')
    docs = yaml.safe_load(f)
    print(docs)
# %%
