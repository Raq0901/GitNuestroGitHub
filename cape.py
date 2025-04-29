import requests, zipfile, os, shutil, glob, yara

def create(folder):
        if not os.path.exists(folder):
                os.mkdir(folder)

def copyfiles(src, dst):
        for root, dirs, files in os.walk(src):
            for filename in files:
                if ('.yara' in filename or '.yar' in filename):
                    shutil.copy(os.path.join(root, filename), os.path.join(dst, filename))

def unzip(filename, dst):
	with zipfile.ZipFile(filename, 'r') as zip_ref:
		zip_ref.extractall(dst)

def download(dst, path):
	r = requests.get(path)
	open(dst, 'wb').write(r.content)

def compile(filepaths, save_folder):
	compiled_rules = dict()
	for folder in filepaths:
		for filename in glob.glob(folder + '/*.yar*'):
			namespace = os.path.basename(os.path.splitext(filename)[0])
			compiled_rules[namespace] = filename
	rules = yara.compile(filepaths = compiled_rules)
	print(compiled_rules)
	if os.path.exists(save_folder):
		os.remove(save_folder)
	rules.save(save_folder)

root = os.path.dirname(os.path.abspath(__file__))
compiled_rules = os.path.join(root, "rules", "rules-compiled")

# Zip filename
cape_filename = os.path.join(root, 'CAPEv2.zip')
reversinglabs_filename = os.path.join(root, 'reversinglabs-yara-rules-develop.zip')
apophis_filename = os.path.join(root, 'apophis-YARA-Rules-main.zip')
countermeasures_filename = os.path.join(root, 'red_team_tool_countermeasures-master.zip')
rulesmaster_filename = os.path.join(root, 'rules-master.zip')
ThreatHunting_filename = os.path.join(root, 'ThreatHunting-Keywords-yara-rules-main.zip')
yaramain_filename = os.path.join(root, 'yara-main.zip')
yararules2025_filename = os.path.join(root, 'Yara_Rules_2025-main.zip')
yararulesmain_filename = os.path.join(root, 'yara_rules-main.zip')
yararulesmaster_filename = os.path.join(root, 'yara-rules-master.zip')
Yararulesmaster_filename = os.path.join(root, 'Yara-rules-master.zip')



# Folder unzip
capev2_folder = os.path.join(root, 'CAPEv2-master')
yara_cape_folder = os.path.join(root, 'CAPEv2-master', 'data', 'yara', 'CAPE')
reversinglab_folder = os.path.join(root, 'reversinglabs-yara-rules-develop')
yara_reversinglab_folder = os.path.join(root, 'reversinglabs-yara-rules-develop', 'yara')
apophis_folder = os.path.join(root, 'apophis-YARA-Rules-main')
yara_apophis_folder = os.path.join(root, 'apophis-YARA-Rules-main', 'YARA-rules')
countermeasures_folder = os.path.join(root, 'red_team_tool_countermeasures-master')
yara_countermeasures_folder = os.path.join(root, 'red_team_tool_countermeasures-master', 'rules')
rulesmaster_folder = os.path.join(root, 'rules-master')
yara_rulesmaster_folder = os.path.join(root, 'rules-master')
ThreatHunting_folder = os.path.join(root, 'ThreatHunting-Keywords-yara-rules-main')
yara_ThreatHunting_folder = os.path.join(root, 'ThreatHunting-Keywords-yara-rules-main')
yaramain_folder = os.path.join(root, 'yara-main')
yara_yaramain_folder = os.path.join(root, 'yara-main')
yararules2025_folder = os.path.join(root, 'Yara_Rules_2025-main')
yara_yararules2025_folder = os.path.join(root, 'Yara_Rules_2025-main', 'Rules_for_January')
yararulesmain_folder = os.path.join(root, 'yara_rules-main')
yara_yararulesmain_folder = os.path.join(root, 'yara_rules-main')
yararulesmaster_folder = os.path.join(root, 'yara-rules-master')
yara_yararulesmaster_folder = os.path.join(root, 'yara-rules-master')
Yararulesmaster_folder = os.path.join(root, 'Yara-rules-master')
yara_Yararulesmaster_folder = os.path.join(root, 'Yara-rules-master', 'rules')




# Local folders
local_cape_folder = os.path.join(root, 'rules', 'Cape')
local_reversinglabs_folder = os.path.join(root, 'rules', 'ReversingLabs')
local_apophis_folder = os.path.join(root, 'rules', 'Apophis')
local_countermeasures_folder = os.path.join(root, 'rules', 'RedTeamContermeasures')
local_rulesmaster_folder = os.path.join(root, 'rules', 'RulesMaster')
local_ThreatHunting_folder = os.path.join(root, 'rules', 'ThreatHunting')
local_yaramain_folder = os.path.join(root, 'rules', 'Yaramain')
local_YaraRules2025_folder = os.path.join(root, 'rules', 'YaraRules2025')
local_yararulesmain_folder = os.path.join(root, 'rules', 'Yararulesmain')
local_yararulesmaster_folder = os.path.join(root, 'rules', 'Yararulesmaster')
local_Yararulesmaster_folder = os.path.join(root, 'rules', 'YaraRulesmaster')


# Directories to compile
directories = [local_cape_folder, local_reversinglabs_folder, local_apophis_folder, local_countermeasures_folder, local_rulesmaster_folder, local_ThreatHunting_folder, local_yaramain_folder, 
local_YaraRules2025_folder, local_yararulesmain_folder, local_yararulesmaster_folder, local_Yararulesmaster_folder,]
# CAPEv2 
create(folder=local_cape_folder)
download(dst=cape_filename, path='https://codeload.github.com/kevoreilly/CAPEv2/zip/refs/heads/master')
unzip(filename=cape_filename, dst=root)
shutil.copytree(src=yara_cape_folder, dst=local_cape_folder, dirs_exist_ok=True)
shutil.rmtree(capev2_folder)
os.remove(cape_filename)

#ReversingLabs
create(folder=local_reversinglabs_folder)
download(dst=reversinglabs_filename, path='https://codeload.github.com/reversinglabs/reversinglabs-yara-rules/zip/refs/heads/develop')
unzip(filename=reversinglabs_filename, dst=root)
copyfiles(src=yara_reversinglab_folder, dst=local_reversinglabs_folder)
shutil.rmtree(reversinglab_folder)
os.remove(reversinglabs_filename)


#Apophis
create(folder=local_apophis_folder)
download(dst=apophis_filename, path='https://github.com/apophis133/apophis-YARA-Rules/archive/refs/heads/main.zip')
unzip(filename=apophis_filename, dst=root)
copyfiles(src=yara_apophis_folder, dst=local_apophis_folder)
shutil.rmtree(apophis_folder)
os.remove(apophis_filename)


#RedTeamCountermeasures
create(folder=local_countermeasures_folder)
download(dst=countermeasures_filename, path='https://github.com/mandiant/red_team_tool_countermeasures/archive/refs/heads/master.zip')
unzip(filename=countermeasures_filename, dst=root)
shutil.copytree(src=yara_countermeasures_folder, dst=local_countermeasures_folder, dirs_exist_ok=True)
shutil.rmtree(countermeasures_folder)
os.remove(countermeasures_filename)

#rulesmaster
create(folder=local_rulesmaster_folder)
download(dst=rulesmaster_filename, path='https://github.com/Yara-Rules/rules/archive/refs/heads/master.zip')
unzip(filename=rulesmaster_filename, dst=root)
shutil.copytree(src=yara_rulesmaster_folder, dst=local_rulesmaster_folder, dirs_exist_ok=True)
shutil.rmtree(rulesmaster_folder)
os.remove(rulesmaster_filename)


#ThreatHunting
create(folder=local_ThreatHunting_folder)
download(dst=ThreatHunting_filename, path='https://github.com/mthcht/ThreatHunting-Keywords-yara-rules/archive/refs/heads/main.zip')
unzip(filename=ThreatHunting_filename, dst=root)
shutil.copytree(src=yara_ThreatHunting_folder, dst=local_ThreatHunting_folder, dirs_exist_ok=True)
shutil.rmtree(ThreatHunting_folder)
os.remove(ThreatHunting_filename)


#yaramain
create(folder=local_yaramain_folder)
download(dst=yaramain_filename, path='https://github.com/securitymagic/yara/archive/refs/heads/main.zip')
unzip(filename=yaramain_filename, dst=root)
shutil.copytree(src=yara_yaramain_folder, dst=local_yaramain_folder, dirs_exist_ok=True)
shutil.rmtree(yaramain_folder)
os.remove(yaramain_filename)

#YaraRules2025
create(folder=local_YaraRules2025_folder)
download(dst=yararules2025_filename, path='https://github.com/shsameer786/Yara_Rules_2025/archive/refs/heads/main.zip')
unzip(filename=yararules2025_filename, dst=root)
shutil.copytree(src=yara_yararules2025_folder, dst=local_YaraRules2025_folder, dirs_exist_ok=True)
shutil.rmtree(yararules2025_folder)
os.remove(yararules2025_filename)


#yararulesmain
create(folder=local_yararulesmain_folder)
download(dst=yararulesmain_filename, path='https://github.com/f0wl/yara_rules/archive/refs/heads/main.zip')
unzip(filename=yararulesmain_filename, dst=root)
shutil.copytree(src=yara_yararulesmain_folder, dst=local_yararulesmain_folder, dirs_exist_ok=True)
shutil.rmtree(yararulesmain_folder)
os.remove(yararulesmain_filename)

#yararulesmaster
create(folder=local_yararulesmaster_folder)
download(dst=yararulesmaster_filename, path='https://github.com/DarkenCode/yara-rules/archive/refs/heads/master.zip')
unzip(filename=yararulesmaster_filename, dst=root)
shutil.copytree(src=yara_yararulesmaster_folder, dst=local_yararulesmaster_folder, dirs_exist_ok=True)
shutil.rmtree(yararulesmaster_folder)
os.remove(yararulesmaster_filename)


#Yararulesmaster
create(folder=local_Yararulesmaster_folder)
download(dst=Yararulesmaster_filename, path='https://github.com/bartblaze/Yara-rules/archive/refs/heads/master.zip')
unzip(filename=Yararulesmaster_filename, dst=root)
shutil.copytree(src=yara_Yararulesmaster_folder, dst=local_Yararulesmaster_folder, dirs_exist_ok=True)
shutil.rmtree(Yararulesmaster_folder)
os.remove(Yararulesmaster_filename)





compile(filepaths=directories, save_folder=compiled_rules)



