#gitManage.py
import requests

class gitManage : 

    def __init__(self,username,repository,token) :
    
        self.__username   = username
        self.__repository = repository
        self.__token      = token

# =============== listBranches _==============================
    def list_branches(self):

        base_url = "https://api.github.com"
        endpoint = f"/repos/{self.__username}/{self.__repository}/branches"
        print(self.__token)
        
        headers = {}
        if self.__token :
            headers["Authorization"] = f"Bearer {self.__token}"
        
        url = f"{base_url}{endpoint}"
        print(url)
        try:
            response = requests.get(url, headers=headers)
            print(response.json())
            response.raise_for_status()
            branches = [ branch["name"] for branch in response.json() ]
        
            return branches

        except requests.exceptions.RequestException as e:
            print("Erro na requisição:", e)
            return None
        except ValueError as e:
            print("Erro de decodificação JSON:", e)
            return None

# ====================== Get Content File =========================================
    def list_files(self):
        base_url = "https://api.github.com"
        endpoint = f"/repos/{self.__username}/{self.__repository}/contents/"
        #endpoint = f"/repos/{username}/{repository}/contents/{filepath=""}"

        headers = {}
        if self.__token :
            headers["Authorization"] = f"Bearer {self.__token}"

        url = f"{base_url}{endpoint}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            content_info = response.json()

            if response.status_code == 200 :
                files = []
                for i_file in content_info : 
                    files.append(i_file["name"])
            
                return files
            else:
                print("File not found")
                return None

        except requests.exceptions.RequestException as e:
            print("Request Error:", e)
            return None
        except ValueError as e:
            print("JSON decod Error:", e)
            return None
        except Exception as e:
            print("Unknown Error:", e)
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
