import { Component, OnInit } from '@angular/core';
import { Usuario } from '../schema/usuario';
import { UsuariosService } from '../services/usuarios.service';

@Component({
  selector: 'app-usuarios',
  templateUrl: './usuarios.component.html',
  styleUrls: ['./usuarios.component.scss']
})
export class UsuariosComponent implements OnInit {

  usuarios: Usuario[] = [];

  constructor(private usuarioService: UsuariosService) {}

  ngOnInit(): void {

    this.usuarioService.usuarios().subscribe(usuarios => this.usuarios = usuarios)
    
  }

}
