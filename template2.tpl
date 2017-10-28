%include('header.tpl')
<h1>Resultado de Mongo</h1>
	%for resultado in result:
		<h5>{{resultado}}</h5>
	%end
%include('footer.tpl')