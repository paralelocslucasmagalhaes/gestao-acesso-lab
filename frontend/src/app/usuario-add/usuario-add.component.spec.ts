import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UsuarioAddComponent } from './usuario-add.component';

describe('UsuarioAddComponent', () => {
  let component: UsuarioAddComponent;
  let fixture: ComponentFixture<UsuarioAddComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UsuarioAddComponent]
    });
    fixture = TestBed.createComponent(UsuarioAddComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
