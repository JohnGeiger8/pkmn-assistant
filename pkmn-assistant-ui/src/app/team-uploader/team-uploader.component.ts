import { Component } from '@angular/core';
import { TeamUploaderService } from './team-uploader.service';

@Component({
  selector: 'app-team-uploader',
  imports: [],
  templateUrl: './team-uploader.component.html',
  styleUrl: './team-uploader.component.scss'
})
export class TeamUploaderComponent {
  selected: File|null = null;
  results: any;
  constructor(private uploader: TeamUploaderService) {}

  onFile(e: Event) {
    this.selected = (e.target as HTMLInputElement).files?.[0] || null;
  }
  
  upload() {
    if (!this.selected) return;
    this.uploader.analyzeTeam(this.selected).subscribe(res => this.results = res);
  }
}
