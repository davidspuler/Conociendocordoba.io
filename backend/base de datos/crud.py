import  mysql.conecctor

class Conectar():
	
			def _init_(self) -> None:
				try:
					self..conexion = mysql..connector. connect(
					
							host =  ˆlocalhostˆ ,
							port = 3306,
							user  = ˆrootˆ ,
							password =  ˆcontraseñaBBDDˆ ,
							db = ˆMiBaseDeDatosˆ
							
							)
					except mysql.connector.Error as  descripcionError
							print (""¡ No se conecto!" ,descripcionError")
							
				def InsertarRegistro(self):
					if self.conexion.is_connected():
						try:
							cursor =  self.conexion.cursor()
							usuario= "INSERT INTO registro VALUES(ˆNombreˆ ,"Apellido ", "Mail","Contraseña"")"
							data= (nombre,apellido,mail,contraseña)
							
							cursor.execute(usuario,data)
							self.conexion.commit()
							self.conexion.close()
							
							except:
								print( "Conexion realizada" )
								
								
								def ActualizarRegistro(self):
									if self.conexion.is_connected():
										try:
											cursor= self.conexion.cursor()
											usuario= "UPDATE  nombre, apellido SET mail,contraseña WHERE id_registro"
											cursor.execute(usuario)
											self.conexion.commit()
											
											self.conexion.close()
											
					except:
								print("Conexion realizada"")
								
								def BuscarRegistro(self):
									if self.conexion. is_connected():
										try:
											cursor = self.connexion.cursor()
											usuario= "SELECT  * from registro where  nombre,apellido,mail.contraseña""
											cursor.execute(usuario)
											resltadoREAD = cursor.fetchall()
											
										return resultadoREAD
										
										self.conexion.close()
											
											
										except:
											print("Conexion realizada")
											
											
						def EliminaRegistro(self,ID):
							if self.conexion. is_connected():
								try:
									cursosr = self.conexion.cursor()
									usuario =  "DELETE from registro where id= IDregistro""
									cursor..execute(usuario)
									
									
									self.connexion.commit()
									self.conexion.close()
						except:
							print("Conexion realizada")
							