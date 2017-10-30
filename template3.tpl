%include('header.tpl')
<h1>Resultado de Mongo</h1>
	%for i in cursor:
			<h3>{{i['city']}}
			{{i['state']}}
			{{i['pop']}}
			{{i['loc']}}</h3><br>
	%end
%include('footer.tpl')