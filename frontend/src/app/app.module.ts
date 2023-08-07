import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { HomeComponent } from './home/home.component';
import { UsuariosComponent } from './usuarios/usuarios.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SharedModule } from './shared/shared.module';
import { HttpClientModule } from '@angular/common/http';
import { UsuariosService } from './services/usuarios.service';
import { UsuarioAddComponent } from './usuario-add/usuario-add.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DepartamentosComponent } from './departamentos/departamentos.component';
import { DepartamentoAddComponent } from './departamento-add/departamento-add.component';
import { DepartamentoService } from './services/departamento.service';



@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    UsuariosComponent,
    UsuarioAddComponent,
    DepartamentosComponent,
    DepartamentoAddComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    SharedModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [UsuariosService, DepartamentoService],
  bootstrap: [AppComponent]
})
export class AppModule { }
