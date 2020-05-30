<?php  include "../core/classeC.php";  ?>
<?php
$Voiture=new VoitureC();
$listeVoiture=$Voiture->affichVoiture();
if(isset($_POST['marque'])) {
	foreach($listeVoiture as $row){ 
		if($_POST['marque']==$row['marque']){ ?>
	<option   value="<?php echo $row['modele']; ?>"> <?php echo $row['modele']; ?></option>
	<?php }}
  }?>
<?php else {
  header('location: ./');
}
?>