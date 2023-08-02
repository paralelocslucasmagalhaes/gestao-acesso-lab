import { Injectable } from '@angular/core';
import { Usuario } from '../schema/usuario';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { API } from './app.api';


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

  add(usuario: Usuario): Observable<Usuario>{
    return this.http.post<Usuario>(`${API}/usuario`, usuario)
  }


}
