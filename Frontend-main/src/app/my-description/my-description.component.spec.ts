import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyDescriptionComponent } from './my-description.component';

describe('MyDescriptionComponent', () => {
  let component: MyDescriptionComponent;
  let fixture: ComponentFixture<MyDescriptionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MyDescriptionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MyDescriptionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
