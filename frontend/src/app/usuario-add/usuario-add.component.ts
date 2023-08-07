import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { UsuariosService } from '../services/usuarios.service';
import { Usuario } from '../schema/usuario';
import { DepartamentoService } from '../services/departamento.service';
import { Departamento } from '../schema/departamento';


@Component({
  selector: 'app-usuario-add',
  templateUrl: './usuario-add.component.html',
  styleUrls: ['./usuario-add.component.scss']
})
export class UsuarioAddComponent   implements OnInit {

  usuarioForm: FormGroup = new FormGroup({});
  departamentos: Departamento[] = [];

  constructor(private usuariosService: UsuariosService,
              private departamentoService: DepartamentoService,
              private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.usuarioForm = this.formBuilder.group({
      email: this.formBuilder.control('', [Validators.email, Validators.required]),
      nome: this.formBuilder.control(''),
      id_departamento: this.formBuilder.control(''),
      ativo: true,
    });
    this.departamentoService.departamentos().subscribe(departamentos => this.departamentos = departamentos);
  }


  add(item: Usuario){
    this.usuariosService.add(item)
      .subscribe(resp => {
        console.log(`Cadastrado com sucesso: ${resp.id}`);
      });
    this.cancel();
  }

  cancel() {
    this.usuarioForm.reset();
  }


}