import os
import pysvn
import git

def ssl_server_trust_prompt( trust_dict ):
    return True, 0, True

svn_client = pysvn.Client()
svn_client.callback_ssl_server_trust_prompt = ssl_server_trust_prompt

def pre_build_fetch():
    if os.path.exists("mangos"):
        print ("Updating MaNGOS sourcecode")
        os.chdir("mangos")
        git.Git('.').pull('-u')
    else:
        print ("MaNGOS is not present; checking out MaNGOS")
        git.Git('.').clone('git://github.com/mangos/mangos.git')
        os.chdir("mangos")

    if os.path.exists("src/bindings/ScriptDev2"):
        print ("Updating ScriptDev2 sourcecode")
        svn_client.update('./src/bindings/ScriptDev2')
    else:
        print ("ScriptDev2 is not present; checking out ScriptDev2")
        os.mkdir("src/bindings/ScriptDev2")
        svn_client.checkout('https://scriptdev2.svn.sourceforge.net/svnroot/scriptdev2', 'src/bindings/ScriptDev2')
        git.Git('.').apply('src/bindings/ScriptDev2/patches/'+my_args.sd2_patch)


def post_build_fetch():
    if os.path.exists("sd2-acid"):
        print ("Updating ACID sourcecode")
        svn_client.update('./sd2-acid')
    else:
        print ("ACID is not present; checking out ACID")
        svn_client.checkout('https://sd2-acid.svn.sourceforge.net/svnroot/sd2-acid', './sd2-acid')

    if os.path.exists("unifieddb"):
        print ("Updating UDB sourcecode")
        svn_client.update('./unifieddb')
    else:
        print ("UDB is not present; checking out UDB")
        svn_client.checkout('https://unifieddb.svn.sourceforge.net/svnroot/unifieddb/trunk', './unifieddb')
