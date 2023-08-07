import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DepartamentoService } from '../services/departamento.service';
import { Departamento } from '../schema/departamento';

@Component({
  selector: 'app-departamento-add',
  templateUrl: './departamento-add.component.html',
  styleUrls: ['./departamento-add.component.scss']
})
export class DepartamentoAddComponent implements OnInit{

  departamentoForm: FormGroup = new FormGroup({});

  constructor(private departamentoService: DepartamentoService,
              private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.departamentoForm = this.formBuilder.group({
      nome: this.formBuilder.control('', Validators.required),
      ativo: true,
    });
  }


  add(item: Departamento){
    this.departamentoService.add(item)
      .subscribe(resp => {
        console.log(`Departamento com sucesso: ${resp.id}`);
      });
    this.cancel();
  }

  cancel() {
    this.departamentoForm.reset();
  }



}
