import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CallComponentsComponent } from './call-components.component';

describe('CallComponentsComponent', () => {
  let component: CallComponentsComponent;
  let fixture: ComponentFixture<CallComponentsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CallComponentsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CallComponentsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
