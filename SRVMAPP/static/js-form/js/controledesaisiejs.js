function verif()
{

	if(document.f.marque.value=="")
	{
		document.getElementById("alerte").innerHTML="Ce champs ne doit pas étre vide ! ";
	}
	if(document.f.modele.value=="")
	{
		document.getElementById("alerte").innerHTML="Ce champs ne doit pas étre vide ! ";
	}

}