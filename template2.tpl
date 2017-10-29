%include('header.tpl')
<h1>Resultado de Mongo</h1>
	%for resultado in cursor:
		{{resultado}}
	%end
%include('footer.tpl')