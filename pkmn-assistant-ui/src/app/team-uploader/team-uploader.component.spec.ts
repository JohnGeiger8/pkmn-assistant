import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamUploaderComponent } from './team-uploader.component';

describe('TeamUploaderComponent', () => {
  let component: TeamUploaderComponent;
  let fixture: ComponentFixture<TeamUploaderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TeamUploaderComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TeamUploaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
