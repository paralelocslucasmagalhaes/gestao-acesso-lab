import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { UsuariosService } from '../services/usuarios.service';
import { Usuario } from '../schema/usuario';


@Component({
  selector: 'app-usuario-add',
  templateUrl: './usuario-add.component.html',
  styleUrls: ['./usuario-add.component.scss']
})
export class UsuarioAddComponent   implements OnInit {

  usuarioForm: FormGroup = new FormGroup({});

  constructor(private usuariosService: UsuariosService,
              private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.usuarioForm = this.formBuilder.group({
      email: this.formBuilder.control('', [Validators.email, Validators.required]),
      nome: this.formBuilder.control(''),
      id_departamento: this.formBuilder.control(''),
      ativo: true,
    });
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