#BOTの使い方

ツイッターのつぶやきを行う機構をRabbitMQを利用したシステムで構成する。

##仕組み
　システムをサーバ側とクライアント側に分けクライアント側が投げたアクションのパラメータをサーバ側がjinjaテンプレートによりレンダリングしツイートする機構を取る
　
##アクションとは
　ツイートを行う一つの単位、アクションには以下のパラメータを渡すことが出来る。  
パラメータはPythonのディクショナリ形式でjinja2テンプレートに渡される。

##利用方法
###サーバの動かし方  

	python bot_server.py  


###クライアントからサーバへのアクションの送り方
	import tweet_bot.bot_client as bot_client
	bot_client.tweet("render_template_name", problem=problem, user=user, answer=answer)
第一引数にはレンダリングを行いたいテンプレートの拡張子を除いた名前を入力する。

###テンプレートの例
	{{ problem.name }}のランキングで{{ user.name }}さんが一位になりました。http://j.mp/1myGxjU #procon25

