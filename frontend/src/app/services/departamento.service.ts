import { Injectable } from '@angular/core';
import { Departamento } from '../schema/departamento';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { API } from './app.api';

@Injectable({
  providedIn: 'root'
})
export class DepartamentoService {

  constructor(
    private http: HttpClient

) { }

departamentos(): Observable<Departamento[]> {
  return this.http.get<Departamento[]>(`${API}/departamento`);
}  

add(departamento: Departamento): Observable<Departamento>{
  return this.http.post<Departamento>(`${API}/departamento`, departamento)
}
}
