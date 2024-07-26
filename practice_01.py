print('hello world')
# git config --global user.email moses@rexsw.com
# git config --global user.name moses
# git remote add origin https://github.com/moses-song/COPD.git
# git branch -M main
# git push -u origin main
# 자동으로 pull request되는건가?

'''기존 연결되어 있는 repository에서 다시 새로운 러퍼지토리에 소스코드를 올리려고 하니 
"error: remote origin already exists."
위와 같은 error발생
해결: 
->  git remote remove origin 으로 기존 열결을 끊어주고
-> git remote add origin https://github.com/moses-song/COPD.git 로 새롭게  연결할 깃 레퍼지토리 주소 명령어를 입력
-> git remote -v 를 입력해 로컬저장소를 원격저장소에 연결
-> git push -u origin main 을 입력하니 또다시 아래같은 error발생

error: failed to push some refs to 'https://github.com/moses-song/COPD.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
-> 원격저장소(github)에 내 로컬(내컴퓨터)에 없는 파일이 있을 때 파일을 push하면 발생하는 오류.
-> 원격저장소에서 내 로컬에 저장하지 않은 파일을 pull한 후 원격저장소에 다시 push를 해야함.
-> git pull origin main 실행한 뒤 다시 push하면 됨.'''
