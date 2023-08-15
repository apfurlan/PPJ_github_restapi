#gitManage.py
import requests
import base64

class gitManage : 

    def __init__(self,username,repository,token,filepath
                 ,base_tree_sha,new_file_path
                 ,new_file_content,commit_message) :
    
        self.__username   = username
        self.__repository = repository
        self.__token      = token
        self.__filepath   = filepath
        self.__base_tree_sha    = base_tree_sha
        self.__new_file_path    = new_file_path
        self.__new_file_content = new_file_content
        self.__commit_message   = commit_message 
        #self.__parent_commit_sha= parent_commit_sha
 
# ================= GET METHODS =============================
# ==================== listBranches ==========================
    def get_branches(self):

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

# ====================== List files =========================================
    def get_files(self):
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
        
# ========================= Get File Content ==========================
    def get_file_content(self):
        base_url = "https://api.github.com"
        endpoint = f"/repos/{self.__username}/{self.__repository}/contents/{self.__filepath}"
        
        headers = {}
        if self.__token :
            headers["Authorization"] = f"Bearer {self.__token}"
        
        url = f"{base_url}{endpoint}"

        response = requests.get(url, headers=headers)

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            if response.status_code == 200 :
                content = response.json().get("content")
                content_bytes = content.encode("utf-8")
                return base64.b64decode(content_bytes).decode("utf-8")
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

# ======================= GET CURRENT TREE SHA =========================
    def get_current_tree_sha(self,branch_name):
        url = f"https://api.github.com/repos/{self.__username}/{self.__repository}/git/refs/heads/{branch_name}"
        headers = {
            "Authorization": f"Bearer {self.__token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        response = requests.get(url, headers=headers)
        response_data = response.json()
        
        if response.status_code == 200:
            return response_data["object"]["sha"]
        else:
            print(f"Error getting current tree SHA: {response_data}")
            return None

# ================= CREATE TREE WITH ALL FILES (git add . ) ============= 
    
    def create_tree_with_all_files(self,base_tree_sha):
        url = f"https://api.github.com/repos/{self.__username}/{self.__repository}/git/trees"
        headers = {
            "Authorization": f"Bearer {self.__token}",
            "Accept": "application/vnd.github.v3+json"
        }

        # Get the existing tree details
        response = requests.get(f"https://api.github.com/repos/{self.__username}/{self.__repository}/git/trees/{base_tree_sha}", headers=headers)
        response_data = response.json()
        existing_tree = response_data.get("tree", [])

        # Add the new file to the existing tree
        new_tree = existing_tree + [{
            "path": self.__new_file_path,
            "mode": "100644",  # File mode
            "type": "blob",
            "content": self.__new_file_content
        }]
        
        data = {
            "base_tree": base_tree_sha,
            "tree": new_tree
        }
        
        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()
        
        if response.status_code == 201:
            return response_data.get("sha")
        else:
            print(f"Error creating tree: {response_data}")
            return None

    # ==============================================================
    def get_branch_sha(self,branch_name):
        
        url = f"https://api.github.com/repos/{self.__username}/{self.__repository}/git/refs/heads/{branch_name}"
        headers = {
            "Authorization": f"Bearer {self.__token}",
            "Accept": "application/vnd.github.v3+json"
        }

        response = requests.get(url, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            return response_data["object"]["sha"]
        else:
            print(f"Error getting branch SHA: {response_data}")
            return None

# ========================== POST METHODS ==============================
# ========================== POST TREE ==========================
    def post_create_new_branch(self,new_branch) :
    
        url = f"https://api.github.com/repos/{self.__username}/{self.__repository}/git/refs"
        headers = {
            "Authorization": f"Bearer {self.__token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        base_branch_sha = self.get_branch_sha("main")

        data = {
            "ref": f"refs/heads/{new_branch}",
            "sha": base_branch_sha
        }

        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()

        if response.status_code == 201:
            return response_data.get("object", {}).get("sha")
        else:
            print(f"Error creating branch: {response_data}")
            return None

    
    def post_create_tree(self):
        
        url = f"https://api.github.com/repos/{self.__username}/{self.__repository}/git/trees"
        headers = {
            "Authorization": f"Bearer {self.__token}",
            "Accept": "application/vnd.github.v3+json"
        }
        new_tree = [{
            "path": self.__new_file_path,
            "mode": "100644",  # File mode
            "type": "blob",
            "content": self.__new_file_content
        }]
        data = {
            "base_tree": self.__base_tree_sha,
            "tree": new_tree
        }
        
        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()
        
        if response.status_code == 201:
            return response_data.get("sha")
        else:
            print(f"Error creating tree: {response_data}")
            return None

# ==================== post commit ===============================
    def post_create_commit(self,tree_sha,parent_commit_sha):
    
        url = f"https://api.github.com/repos/{self.__username}/{self.__repository}/git/commits"
        headers = {
            "Authorization": f"Bearer {self.__token}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {
            "message": self.__commit_message,
            "tree": tree_sha,
            "parents": [parent_commit_sha]
        }
        
        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()
        
        if response.status_code == 201:
            return response_data.get("sha")
        else:
            print(f"Error creating commit: {response_data}")
            return None


#======================================================
    def patch_update_branch_reference(self,branch_name,new_commit_sha) :
        # owner, repo, branch_name, new_commit_sha, access_token):
        url = f"https://api.github.com/repos/{self.__username}/{self.__repository}/git/refs"
        
        headers = {
            "Authorization": f"Bearer {self.__token}",
            "Accept": "application/vnd.github.v3+json"
        }

        data = {
            "sha": new_commit_sha,
            "ref": f"refs/heads/{branch_name}"   
        }
        
        response = requests.patch(url, json=data, headers=headers)
        
        if response.status_code == 200 or response.status_code == 201 :
            print("Commit successful!")
        else:
            print(f"Error updating branch reference: {response.status_code}")

