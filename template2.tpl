%include('header.tpl')
<h1>Resultado de Mongo</h1>
	%for i in cursor:
		{{i}}
	%end
%include('footer.tpl')