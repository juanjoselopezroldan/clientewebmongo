%include('header.tpl')
<h1>Resultado de Mongo</h1>
	%for i in cursor:
			<h3>Ciudad: {{i['city']}}
			Estado: {{i['state']}}
			Poblacion: {{i['pop']}}
			Localizacion: {{i['loc']}}</h3><br>
	%end
%include('footer.tpl')