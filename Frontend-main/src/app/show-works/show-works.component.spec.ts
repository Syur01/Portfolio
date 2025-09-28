import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowWorksComponent } from './show-works.component';

describe('ShowWorksComponent', () => {
  let component: ShowWorksComponent;
  let fixture: ComponentFixture<ShowWorksComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ShowWorksComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowWorksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
