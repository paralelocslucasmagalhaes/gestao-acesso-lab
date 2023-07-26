import { Injectable } from '@angular/core';
import { Usuario } from '../schema/usuario';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { API } from './app.api';


const USUARIO_DATA: Usuario[] = [

  {id: 1, email: "Lucas@ss", nome: "Lucas", departamento: "Tech", ativo: true},
  {id: 2, email: "teste@ss", nome: "Teste", departamento: "Tech", ativo: true},

]

@Injectable({
  providedIn: 'root'
})
export class UsuariosService {

  constructor(
      private http: HttpClient

  ) { }

  usuarios(): Observable<Usuario[]> {
    return this.http.get<Usuario[]>(`${API}/usuario`);
  }  


}
