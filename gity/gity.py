"""
        _ _         
   __ _(_) |_ _   _ 
  / _` | | __| | | |
 | (_| | | |_| |_| |
  \__, |_|\__|\__, |
  |___/       |___/ 


gity : The Git magician for Python

"""

import subprocess
import os


class gity:

    def __init__(self, user='', paswd='', repo=''):
        """ (gity object, user, paswd, repo) -> NoneType

        Initalize with username , password and path to repository
        """

        self.user = user
        self.paswd = paswd

        # check if repositry is a string
        if repo == '':
            self.repo = os.getcwd()
        elif type(repo) == str:
            self.repo = repo
            os.chdir(repo)
        else:
            raise Exception("Expected String")

    def set_user(self, user):
        """(gity object,str) -> NoneType

        set user value to entered String
        """
        try:
            assert type(user) == str
            self.user = user
        except:
            raise Exception("Expected String")

    def set_password(self, paswd):
        """(gity object,str) -> NoneType

        Set password for github account
        """
        try:
            assert type(paswd) == str
            self.paswd = paswd
        except:
            raise Exception("Expected String")

    def set_repository(self, repo):
        """(gity object,str) -> NoneType

        Set path to repository
        """
        try:
            assert type(repo) == str
            self.repo = repo
            os.chdir(repo)
        except:
            raise Exception("Expected String")

    def git_init(self):
        """(gity object) -> bool

        Initalizes git repository at specified path 
        path taken from self.repo
        """
        try:
            args = ["git", "init"]
            state = subprocess.call(args)
            status = True
        except:
            status = False

        return status

    def git_clone(self, url, arg=''):
        """(gity object, str, str) -> bool
        Clones a repository into a newly created directory (path taken from self.repo ), 
        creates remote-tracking branches for each branch in the cloned repository
        """
        if arg != '':
            args.append(arg)
        try:
            args = ["git", "init"]
            state = subprocess.call(args)
            status = True
        except:
            status = False

        return status

    def git_status(self):
        """(gity object) -> str

        Executes command "git status" on command line 
        Prints status of the repository
        Returns True if status is printed
                        False if an exception occurs
        """
        try:
            args = ["git", "status"]
            state = subprocess.call(args)
            status = True
        except:
            status = False

        return status

    def git_add(self, files=[], deletion=False):
        """(gity object, list, bool) -> bool

        Add multiple files in directory.
        Files is the list of files that you want to add.
        If the list is empty, all files in the directory will be added

        Default:
                All files in the directory will be added
                Deleted files will not be tracked/added

        git_add can :
                -> Add multiple files while ignoring deletion
                -> Add/Track all files including deleted
        """

        try:
        # Check if arguments match the expected type
            assert type(files) == list
            assert type(deletion) == bool
        except:
            raise Exception(
                "Files expected as list\ndeletion expected as bool")

        if deletion == True:
        # If deletion is True track all files
            try:
                args = ["git", "add", "-A"]
                state = subprocess.call(args)
                status = True
                print "Added all the files [ including deleted ]"
            except:
                status = False
        else:
        # Deletion is false then
        #	-> Add all files while ignoring deletion
        #	-> Add only specified files while ignoring deletion
            if files == []:
                try:
                    args = ["git", "add", ".", "--ignore-removal"]
                    state = subprocess.call(args)
                    status = True
                    print "Added all the files except deletions"
                except:
                    status = False
            else:
                try:
                    args = ["git", "add"]

                    # Add all the file name to list of args
                    for fi in files:
                        args.append(fi)

                    state = subprocess.call(args)
                    status = True
                    print "Added all the files mentioned"
                except:
                    status = False

            return status

    def git_commit(self, message):
        """(gity object,str) -> bool

        Returns True if commit is succesful
        else returns False.
        """
        if type(message) != str:
            raise Exception("Expected message as string")
        try:
            args = ["git", "commit", "-m", message]
            state = subprocess.call(args)
            status = True
            print "Commit succesful"
        except:
            status = False

        return status

    def git_push(self, remoteName='origin', branchName='master'):
        """ (gity object, str, str) -> bool

        Default:
                pushes origin 
        Returns True if the push is succesful
        else returns False
        """

        try:
            args = ["git", "push", remoteName, branchName]
            state = subprocess.call(args)
            status = True
            print "Push succesful"
        except:
            status = False

        return status

    def git_pull(self):
        """(gity object) -> bool 

        Executes git pull on the mentioned repository
        """
        try:
            args = ["git", "pull"]
            state = subprocess.call(args)
            status = True
            print "Pull succesful"
        except:
            status = False

        return status

    def git_checkout(self, branch):
        """

        Executes git checkout to switch to given branch
        """
        try:
            args = ["git", "checkout", "branch"]
            state = subprocess.call(args)
            status = True
            print "Checkout succesful"
        except:
            status = False

        return status

if __name__ == "__main__":
    print """
	        _ _         
	   __ _(_) |_ _   _ 
	  / _` | | __| | | |
	 | (_| | | |_| |_| |
	  \__, |_|\__|\__, |
	  |___/       |___/ 

	gity : Git Magician for Python

"""
