```css
.container {  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1.4fr 0.6fr 1fr;
  grid-template-rows: 0.4fr 0.5fr 0.6fr 2.3fr 1.2fr 1fr 0.5fr;
  gap: 10px 10px;
  grid-auto-flow: row;
  grid-template-areas:
    "Title Title Title Title Title Title Title Average-Grade Average-Grade Image Image"
    "DropdownMenus DropdownMenus DropdownMenus DropdownMenus DropdownMenus DropdownMenus DropdownMenus DropdownMenus DropdownMenus Image Image"
    "Summary-Table Summary-Table Summary-Table Summary-Table Summary-Table Summary-Table Summary-Table Summary-Table Summary-Table Summary-Table Summary-Table"
    "Summary-Chart Summary-Chart Summary-Chart Summary-Chart Summary-Chart Summary-Chart Summary-Chart Summary-Chart Summary-Chart Summary-Chart Summary-Chart"
    "Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects"
    "Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects"
    "Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects Subjects";
}

.DropdownMenus {  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  gap: 0px 0px;
  grid-auto-flow: row;
  grid-template-areas:
    "Language-Dropdown Student-Drodown Grade-dropdown"
    "Language-Dropdown Student-Drodown Grade-dropdown"
    "Language-Dropdown Student-Drodown Grade-dropdown";
  grid-area: DropdownMenus;
}

.Language-Dropdown { grid-area: Language-Dropdown; }

.Student-Drodown { grid-area: Student-Drodown; }

.Grade-dropdown { grid-area: Grade-dropdown; }

.Summary-Table { grid-area: Summary-Table; }

.Summary-Chart { grid-area: Summary-Chart; }

.Subjects {  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 0.6fr 0.6fr 1.8fr;
  gap: 0px 0px;
  grid-auto-flow: row;
  grid-template-areas:
    "Subjects-Dropdown Subjects-Dropdown Subjects-Dropdown"
    "Subject-Table Subject-Table Subject-Table"
    "Subjects-Chart Subjects-Chart Subjects-Chart";
  grid-area: Subjects;
}

.Subjects-Dropdown { grid-area: Subjects-Dropdown; }

.Subject-Table { grid-area: Subject-Table; }

.Subjects-Chart { grid-area: Subjects-Chart; }

.Image { grid-area: Image; }

.Title { grid-area: Title; }

.Average-Grade { grid-area: Average-Grade; }
```