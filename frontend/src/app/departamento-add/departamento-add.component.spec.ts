import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DepartamentoAddComponent } from './departamento-add.component';

describe('DepartamentoAddComponent', () => {
  let component: DepartamentoAddComponent;
  let fixture: ComponentFixture<DepartamentoAddComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DepartamentoAddComponent]
    });
    fixture = TestBed.createComponent(DepartamentoAddComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
