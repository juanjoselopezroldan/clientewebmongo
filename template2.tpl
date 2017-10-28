%include('header.tpl')
<h1>Resultado de Mongo</h1>
	% for res in cursor:
		<h1>{{res}}</h1>
	%end
%include('footer.tpl')