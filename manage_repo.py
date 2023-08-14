
# %%
import requests
import json 
import base64
from  gitManage import getBranches
#from  gitManage import getFiles

def getFiles(username,repository,token=None):
    base_url = "https://api.github.com"
    endpoint = f"/repos/{username}/{repository}/contents/"
    #endpoint = f"/repos/{username}/{repository}/contents/{filepath=""}"
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    url = f"{base_url}{endpoint}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        content_info = response.json()
        print(response.status_code)

        if response.status_code == 200 :
            files = []
            for i_file in content_info : 
                files.append(i_file["name"])
        
            return files
        else:
            print("Arquivo não encontrado.")
            return None

    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)
        return None
    except ValueError as e:
        print("Erro de decodificação JSON:", e)
        return None
    except Exception as e:
        print("Erro desconhecido:", e)
        return None

# ============================================
import requests

def gitAddAll(owner,repo_name,token=None): #, file_path, branch="main"):
    file_path=""
    branch="main"
    # Base URL da API do GitHub
    base_url = "https://api.github.com"

    # Cabeçalhos da requisição com o token de acesso pessoal
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept" : "application/vnd.github.v3+json" 
    } if token else {}

    # Obtenha a lista de arquivos modificados na árvore de trabalho
    files = []
    git_status = requests.get(f"{base_url}/repos/{owner}/{repo_name}/git/trees/{branch}", headers=headers)
    print(git_status.status_code)
    if git_status.status_code == 200:
        tree = git_status.json().get("tree", [])
        files = [{"path": item["path"], "mode": item["mode"], "type": item["type"]} for item in tree]
        print(files)
    else:
        print(f"Erro ao obter o status do repositório: {git_status.json()}")
        return

    #Dados da requisição para criar o novo commit
    changes = []
    for file in files:
        if file["type"] == "blob":
            file_path = file["path"]
            content = requests.get(f"{base_url}/repos/{owner}/{repo_name}/contents/{file_path}?ref={branch}", headers=headers)
            if content.status_code == 200:
                content = content.json()
                content["content"] = base64.b64encode(content["content"].encode("utf-8")).decode("utf-8")
                changes.append({
                    "path": file_path,
                    "mode": file["mode"],
                    "type": "blob",
                    "content": content["content"]
                })
            else:
                print(f"Erro ao obter o conteúdo do arquivo {file_path}: {content.json()}")
                return

    # Crie um novo commit com as mudanças
    # Get the current file content (for obtaining the SHA hash)
    api_url = 'https://api.github.com/repos/{owner}/{repo_name}/contents/'    
    response = requests.get(api_url, headers=headers)
    data = response.json()
    current_sha = data['sha']




    aaa ="dadwadaw"
    data = {
        "message": "Adicionando mudanças via API do GitHub",
        "content" :  base64.b64encode(aaa.encode()).decode(),
        "parents": [branch],
        "tree": changes,
        "sha" : data["sha"]
    }

    create_commit_url = f"{base_url}/repos/{owner}/{repo_name}/git/commits"
    response = requests.post(create_commit_url, json=data, headers=headers)

    if response.status_code == 201:
        # Atualize a referência da branch com o novo commit
        commit_sha = response.json().get("sha", "")
        update_ref_url = f"{base_url}/repos/{owner}/{repo_name}/git/refs/heads/{branch}"
        ref_data = {
            "sha": commit_sha,
            "force": False
        }
        update_ref = requests.patch(update_ref_url, json=ref_data, headers=headers)

        if update_ref.status_code == 200:
            print("Mudanças adicionadas e commit criado com sucesso!")
        else:
            print(f"Erro ao atualizar a referência da branch: {update_ref.json()}")
    else:
        print(f"Erro ao criar o novo commit: {response.json()}")


username = "apfurlan"
repository = "PPJ_react_dashboard"
token = None

# branches = getBranches(username,repository)
# print(branches)
files = getFiles(username,repository)
#files = getFiles(username,repository)
file_path_to_add = ""
gitAddAll(username,repository,token)

print(files)

# %%

import json
import yaml
import os 
from gitManage import gitManage


home = os.path.expanduser('~') 
with open(f"{home}/my_github_pas.yaml", 'r') as file:
    data = yaml.safe_load(file)

username   = data["gitrepos"]["repo_owner"]
repository = data["gitrepos"]["repo_name"]
token      = data["gitrepos"]["personal_access_token"]["key2"]

githubrepo = gitManage(username,repository,token) 

#tkn = githubrepo.get_token()\
aa = githubrepo.get_branches()
bb = githubrepo.get_files()
print(aa)
print("----------")
print(bb)