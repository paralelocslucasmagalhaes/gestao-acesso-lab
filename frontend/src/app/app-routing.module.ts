import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { UsuariosComponent } from './usuarios/usuarios.component';
import { UsuarioAddComponent } from './usuario-add/usuario-add.component';

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'usuarios', component: UsuariosComponent},
  {path: 'usuarios/new', component: UsuarioAddComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }



