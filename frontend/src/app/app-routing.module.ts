import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { UsuariosComponent } from './usuarios/usuarios.component';
import { UsuarioAddComponent } from './usuario-add/usuario-add.component';
import { DepartamentosComponent } from './departamentos/departamentos.component';
import { DepartamentoAddComponent } from './departamento-add/departamento-add.component';

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'usuarios', component: UsuariosComponent},
  {path: 'usuarios/new', component: UsuarioAddComponent},
  {path: 'departamentos', component: DepartamentosComponent},
  {path: 'departamentos/new', component: DepartamentoAddComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }



