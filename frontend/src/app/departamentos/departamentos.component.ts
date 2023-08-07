import { Component, OnInit } from '@angular/core';
import { Departamento } from '../schema/departamento';
import { DepartamentoService } from '../services/departamento.service';

@Component({
  selector: 'app-departamentos',
  templateUrl: './departamentos.component.html',
  styleUrls: ['./departamentos.component.scss']
})
export class DepartamentosComponent implements OnInit {

  departamentos: Departamento[] = [];

  constructor(private departamentoService: DepartamentoService) {}

  ngOnInit(): void {

    this.departamentoService.departamentos().subscribe(departamentos => this.departamentos = departamentos);
    
  }

}
