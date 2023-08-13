#gitManage.py
import requests

class gitManage() : 

#     # username = "apfurlan"
#     # repository = "PPJ_react_dashboard"
#     # token = None

# def __init__(self,username,repository,token=None) -> None:
    
#     username = username
#     repository = repository
#     token = token

#     return 

# #     listBranches

def getBranches(username,repository,token=None):

    base_url = "https://api.github.com"
    endpoint = f"/repos/{username}/{repository}/branches"
    headers = {
        "Authorization": f"Bearer {token}"
    } if token else {}
    url = f"{base_url}{endpoint}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        branches = [] #response.json()
        for branch in response.json() : 
            branches.append(branch["name"])
        return branches
    

    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)
        return None
    except ValueError as e:
        print("Erro de decodificação JSON:", e)
        return None

# ===============================================================
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
        



#     listContent

# def list_branches(username, repository, token=None):
#     base_url = "https://api.github.com"
#     endpoint = f"/repos/{username}/{repository}/branches"
#     headers = {
#         "Authorization": f"Bearer {token}"
#     } if token else {}
#     url = f"{base_url}{endpoint}"

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         branches = response.json()
#         return [branch["name"] for branch in branches]
#     except requests.exceptions.RequestException as e:
#         print("Erro na requisição:", e)
#         return None
#     except ValueError as e:
#         print("Erro de decodificação JSON:", e)
#         return None



# def create_branch(username, repository, base_branch, new_branch, token=None):
#     base_url = "https://api.github.com"
#     endpoint = f"/repos/{username}/{repository}/git/refs"
#     headers = {"Authorization": f"Bearer {token}"} if token else {}
#     url = f"{base_url}{endpoint}"

#     try:
#         # Primeiro, obtenha o último commit da branch base
#         response = requests.get(f"{base_url}/repos/{username}/{repository}/git/refs/heads/{base_branch}", headers=headers)
#         response.raise_for_status()
#         commit_sha = response.json()["object"]["sha"]

#         # Crie uma nova referência para a nova branch apontando para o mesmo commit
#         data = {
#             "ref": f"refs/heads/{new_branch}",
#             "sha": commit_sha
#         }
#         response = requests.post(url, json=data, headers=headers)
#         response.raise_for_status()

#         print(f"Branch '{new_branch}' criada com sucesso no repositório {username}/{repository}.")
#     except requests.exceptions.RequestException as e:
#         print("Erro na requisição:", e)
#     except ValueError as e:
#         print("Erro de decodificação JSON:", e)
#     except Exception as e:
#         print("Erro desconhecido:", e)


# def get_file_content(username, repository, filepath, token=None):
#     base_url = "https://api.github.com"
#     endpoint = f"/repos/{username}/{repository}/contents/{filepath}"
#     headers = {"Authorization": f"Bearer {token}"} if token else {}
#     url = f"{base_url}{endpoint}"

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         content_info = response.json()
#         print(response.status_code)

#         if response.status_code == 200 :
#             files = []
#             for i_file in content_info : 
#                 files.append(i_file["name"])
        
#             return files
#         else:
#             print("Arquivo não encontrado.")
#             return None

#     except requests.exceptions.RequestException as e:
#         print("Erro na requisição:", e)
#         return None
#     except ValueError as e:
#         print("Erro de decodificação JSON:", e)
#         return None
#     except Exception as e:
#         print("Erro desconhecido:", e)
#         return None


# url = "https://github.com/apfurlan/PPJ_react_dashboard"

# # aa = requests.get(url)
# # print(aa.json())

# file_obj = open("/home/apfurlan/my_github_pas","r")

# OWNER = "apfurlan"
# REPO = "PPJ_react_dashboard"
# BASE_BRANCH = "main"  # Branch existente que servirá de base
# NEW_BRANCH = "feat/branch-test"  # No

# PAS = file_obj.read() 
# print(PAS)

# #create_branch(OWNER, REPO, BASE_BRANCH, NEW_BRANCH, token=None)

# PAS = None
# branches = list_branches(OWNER, REPO, PAS)
# if branches:
#     print(f"Branches do repositório {OWNER}/{REPO}:")
#     for branch in branches:
#         print(branch)
# else:
#     print("Não foi possível obter a lista de branches.")

# file_content = get_file_content(OWNER,REPO, filepath="/", token=None)
# if file_content:
#     print(f"O conteúdo do repositório {OWNER}/{REPO}:")
#     for files in file_content:
#         print(files)
# else:
#     print("Não foi possível obter os arquivos do repositório.")






# def list_branches(username, repository, token=None):
#     base_url = "https://api.github.com"
#     endpoint = f"/repos/{username}/{repository}/branches"
#     headers = {
#         "Authorization": f"Bearer {token}"
#     } if token else {}
#     url = f"{base_url}{endpoint}"

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         branches = response.json()
#         return [branch["name"] for branch in branches]
#     except requests.exceptions.RequestException as e:
#         print("Erro na requisição:", e)
#         return None
#     except ValueError as e:
#         print("Erro de decodificação JSON:", e)
#         return None



# def create_branch(username, repository, base_branch, new_branch, token=None):
#     base_url = "https://api.github.com"
#     endpoint = f"/repos/{username}/{repository}/git/refs"
#     headers = {"Authorization": f"Bearer {token}"} if token else {}
#     url = f"{base_url}{endpoint}"

#     try:
#         # Primeiro, obtenha o último commit da branch base
#         response = requests.get(f"{base_url}/repos/{username}/{repository}/git/refs/heads/{base_branch}", headers=headers)
#         response.raise_for_status()
#         commit_sha = response.json()["object"]["sha"]

#         # Crie uma nova referência para a nova branch apontando para o mesmo commit
#         data = {
#             "ref": f"refs/heads/{new_branch}",
#             "sha": commit_sha
#         }
#         response = requests.post(url, json=data, headers=headers)
#         response.raise_for_status()

#         print(f"Branch '{new_branch}' criada com sucesso no repositório {username}/{repository}.")
#     except requests.exceptions.RequestException as e:
#         print("Erro na requisição:", e)
#     except ValueError as e:
#         print("Erro de decodificação JSON:", e)
#     except Exception as e:
#         print("Erro desconhecido:", e)


# def get_file_content(username, repository, filepath, token=None):
#     base_url = "https://api.github.com"
#     endpoint = f"/repos/{username}/{repository}/contents/{filepath}"
#     headers = {"Authorization": f"Bearer {token}"} if token else {}
#     url = f"{base_url}{endpoint}"

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         content_info = response.json()
#         print(response.status_code)

#         if response.status_code == 200 :
#             files = []
#             for i_file in content_info : 
#                 files.append(i_file["name"])
        
#             return files
#         else:
#             print("Arquivo não encontrado.")
#             return None

#     except requests.exceptions.RequestException as e:
#         print("Erro na requisição:", e)
#         return None
#     except ValueError as e:
#         print("Erro de decodificação JSON:", e)
#         return None
#     except Exception as e:
#         print("Erro desconhecido:", e)
#         return None


# url = "https://github.com/apfurlan/PPJ_react_dashboard"

# # aa = requests.get(url)
# # print(aa.json())

# file_obj = open("/home/apfurlan/my_github_pas","r")

# OWNER = "apfurlan"
# REPO = "PPJ_react_dashboard"
# BASE_BRANCH = "main"  # Branch existente que servirá de base
# NEW_BRANCH = "feat/branch-test"  # No

# PAS = file_obj.read() 
# print(PAS)

# #create_branch(OWNER, REPO, BASE_BRANCH, NEW_BRANCH, token=None)

# PAS = None
# branches = list_branches(OWNER, REPO, PAS)
# if branches:
#     print(f"Branches do repositório {OWNER}/{REPO}:")
#     for branch in branches:
#         print(branch)
# else:
#     print("Não foi possível obter a lista de branches.")

# file_content = get_file_content(OWNER,REPO, filepath="/", token=None)
# if file_content:
#     print(f"O conteúdo do repositório {OWNER}/{REPO}:")
#     for files in file_content:
#         print(files)
# else:
#     print("Não foi possível obter os arquivos do repositório.")
