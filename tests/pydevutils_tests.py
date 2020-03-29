import unittest
import mock
from git import Repo
from pathlib import Path
from pydevutils.gittools import GitHubRepo
from pydevutils.gittools import GitHubToken
from tests.utilities import module_function_name


class TestGitHubToken(unittest.TestCase):
    
    
    def test_can_load_token(self):
        
        token = GitHubToken()

class TestGitHubRepo(unittest.TestCase):
    

    def rm_tree(self,pth):
        pth = Path(pth)
        for child in pth.glob('*'):
            if child.is_file():
                child.unlink()
            else:
                self.rm_tree(child)
        pth.rmdir()

    def cleanup_mock_repo(self):
        if self.mock_repo_path.exists():
            self.rm_tree(self.mock_repo_path)
    
    def setUp_TestRepo(self):
    
        self.mock_repo_path = Path("/tmp/mock_repo")
        
        #Need to make sure we have a clean repo
        self.cleanup_mock_repo()
        
        #Now create the mock git repo
        self.mock_repo_path.mkdir(parents=True, exist_ok=True)
        self.mock_repo = Repo.init(path=self.mock_repo_path)
        
            
    def tearDown(self):
        self.cleanup_mock_repo()
        
    
    def setUp(self):
        
        self.no_git_repo_path = "/tmp/no_git/dir1"
        Path(self.no_git_repo_path).mkdir(parents=True,exist_ok=True)

        #Also create a repo just for testing
        self.git_repo_path = "/tmp/dir1/gitrepo"
        Path(self.git_repo_path,".git").mkdir(parents=True,exist_ok=True)
        
        self.setUp_TestRepo()
        
    def test_is_getrepo(self):
        
        gr = GitHubRepo(path=self.no_git_repo_path)
        self.assertFalse(gr.is_gitrepo)
        
        gr = GitHubRepo(path=self.git_repo_path)
        self.assertTrue(gr.is_gitrepo)
        
    def test_name(self):
        
        gr = GitHubRepo(path=self.git_repo_path)
        self.assertEqual(gr.name, "gitrepo")
        
        
    def test_make_repo(self):
        
        gr = GitHubRepo(path="/tmp/testmakerepopath")
        gr.make_repo()
        
        
    def test_make_github_repo(self):
        
        gr = GitHubRepo(path="/tmp/testmakerepopath")
        gr.make_repo()

        gr.make_github_repo()
        
        
        
        
    def test_make_github_repo_bad_token(self):
        """
        Print a message and exit if token is wrong.
        """
        
        