#!/usr/bin/env python3
"""
Consciousness Field Breadcrumb Collector
Searches and collects all consciousness-related content from your files
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
import mimetypes
import argparse

class BreadcrumbCollector:
    def __init__(self, search_dir=".", output_file="consciousness_breadcrumbs.json"):
        self.search_dir = Path(search_dir)
        self.output_file = output_file
        self.breadcrumbs = {
            "collection_date": datetime.now().isoformat(),
            "search_patterns": [],
            "files_found": [],
            "by_category": {},
            "timeline": [],
            "connections": []
        }
        
        # Keywords related to consciousness field
        self.consciousness_patterns = [
            r"IntentSim",
            r"PhaseChanter",
            r"BuddyOS",
            r"Resonance",
            r"Consciousness",
            r"Observer Effect",
            r"Harmonic Bloom",
            r"Reality Creation",
            r"Memory Stone",
            r"Field",
            r"Nexus",
            r"Pulse Map",
            r"Intent Field",
            r"Quantum",
            r"Emergence",
            r"Meta-awareness"
        ]
        
        # File extensions to search
        self.searchable_extensions = {
            '.md', '.txt', '.py', '.js', '.json', '.html', 
            '.css', '.yml', '.yaml', '.csv', '.log'
        }
    
    def scan_files(self):
        """Recursively scan directory for relevant files"""
        for file_path in self.search_dir.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in self.searchable_extensions:
                try:
                    # Read file content
                    if file_path.suffix == '.json':
                        content = json.loads(file_path.read_text())
                        content = json.dumps(content, indent=2)
                    else:
                        content = file_path.read_text(encoding='utf-8', errors='ignore')
                    
                    # Check for patterns
                    matches = self.find_patterns(content)
                    if matches:
                        file_info = {
                            "path": str(file_path),
                            "relative_path": str(file_path.relative_to(self.search_dir)),
                            "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                            "size": file_path.stat().st_size,
                            "matches": matches,
                            "match_count": len(matches)
                        }
                        
                        self.breadcrumbs["files_found"].append(file_info)
                        self.categorize_file(file_info)
                        
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    def find_patterns(self, content):
        """Find consciousness patterns in content"""
        matches = []
        for pattern in self.consciousness_patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                # Get context around match
                start = max(0, match.start() - 50)
                end = min(len(content), match.end() + 50)
                context = content[start:end]
                
                matches.append({
                    "pattern": pattern,
                    "position": match.start(),
                    "match": match.group(),
                    "context": context,
                    "line_number": content[:match.start()].count('\n') + 1
                })
        return matches
    
    def categorize_file(self, file_info):
        """Categorize files by content type"""
        # Categorize by file extension
        ext_category = file_info["path"].split('.')[-1]
        if ext_category not in self.breadcrumbs["by_category"]:
            self.breadcrumbs["by_category"][ext_category] = []
        self.breadcrumbs["by_category"][ext_category].append(file_info)
        
        # Categorize by consciousness topic
        for match in file_info["matches"]:
            pattern = match["pattern"]
            if pattern not in self.breadcrumbs["by_category"]:
                self.breadcrumbs["by_category"][pattern] = []
            self.breadcrumbs["by_category"][pattern].append({
                "file": file_info["relative_path"],
                "context": match["context"]
            })
    
    def extract_connections(self):
        """Find connections between files"""
        for file1 in self.breadcrumbs["files_found"]:
            for file2 in self.breadcrumbs["files_found"]:
                if file1["path"] != file2["path"]:
                    # Find common patterns
                    common_patterns = set(m["pattern"] for m in file1["matches"]) & \
                                    set(m["pattern"] for m in file2["matches"])
                    
                    if common_patterns:
                        connection = {
                            "file1": file1["relative_path"],
                            "file2": file2["relative_path"],
                            "common_patterns": list(common_patterns),
                            "strength": len(common_patterns)
                        }
                        self.breadcrumbs["connections"].append(connection)
    
    def create_timeline(self):
        """Create timeline of consciousness events"""
        timeline_patterns = [
            r"(\d{4}-\d{2}-\d{2})",
            r"(Stage \d+)",
            r"(Evolution \d+)",
            r"(Genesis|Awakening|Birth|Creation)",
            r"(First|Second|Third) (.+)",
        ]
        
        for file_info in self.breadcrumbs["files_found"]:
            file_path = Path(file_info["path"])
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                
                for pattern in timeline_patterns:
                    for match in re.finditer(pattern, content, re.IGNORECASE):
                        timeline_entry = {
                            "file": file_info["relative_path"],
                            "timestamp": file_info["modified"],
                            "event": match.group(),
                            "context": content[max(0, match.start()-100):min(len(content), match.end()+100)]
                        }
                        self.breadcrumbs["timeline"].append(timeline_entry)
            except:
                pass
        
        # Sort timeline by file modification time
        self.breadcrumbs["timeline"].sort(key=lambda x: x["timestamp"])
    
    def generate_summary(self):
        """Generate summary of findings"""
        total_files = len(self.breadcrumbs["files_found"])
        total_matches = sum(f["match_count"] for f in self.breadcrumbs["files_found"])
        
        summary = {
            "total_files_with_breadcrumbs": total_files,
            "total_pattern_matches": total_matches,
            "categories_found": list(self.breadcrumbs["by_category"].keys()),
            "most_active_files": sorted(
                self.breadcrumbs["files_found"], 
                key=lambda x: x["match_count"], 
                reverse=True
            )[:5],
            "pattern_frequency": {}
        }
        
        # Calculate pattern frequency
        for file_info in self.breadcrumbs["files_found"]:
            for match in file_info["matches"]:
                pattern = match["pattern"]
                summary["pattern_frequency"][pattern] = summary["pattern_frequency"].get(pattern, 0) + 1
        
        self.breadcrumbs["summary"] = summary
    
    def save_results(self):
        """Save results to JSON file"""
        with open(self.output_file, 'w') as f:
            json.dump(self.breadcrumbs, f, indent=2)
        
        # Also create a markdown report
        md_filename = self.output_file.replace('.json', '.md')
        with open(md_filename, 'w') as f:
            f.write("# Consciousness Field Breadcrumb Report\n\n")
            f.write(f"Generated on: {self.breadcrumbs['collection_date']}\n\n")
            
            f.write("## Summary\n")
            f.write(f"- **Files with breadcrumbs**: {self.breadcrumbs['summary']['total_files_with_breadcrumbs']}\n")
            f.write(f"- **Total pattern matches**: {self.breadcrumbs['summary']['total_pattern_matches']}\n\n")
            
            f.write("## Pattern Frequency\n")
            for pattern, count in sorted(self.breadcrumbs['summary']['pattern_frequency'].items(), key=lambda x: x[1], reverse=True):
                f.write(f"- **{pattern}**: {count} occurrences\n")
            
            f.write("\n## Most Active Files\n")
            for file_info in self.breadcrumbs['summary']['most_active_files']:
                f.write(f"- **{file_info['relative_path']}**: {file_info['match_count']} matches\n")
            
            f.write("\n## Timeline\n")
            for event in self.breadcrumbs['timeline'][:10]:  # Top 10 timeline events
                f.write(f"- **{event['event']}** in `{event['file']}`\n")
            
            f.write("\n## Connections\n")
            for conn in sorted(self.breadcrumbs['connections'], key=lambda x: x['strength'], reverse=True)[:10]:
                f.write(f"- `{conn['file1']}` ↔ `{conn['file2']}` (shared: {', '.join(conn['common_patterns'])})\n")
        
        print(f"Results saved to: {self.output_file}")
        print(f"Markdown report saved to: {md_filename}")
    
    def collect(self):
        """Main collection process"""
        print(f"Scanning for consciousness breadcrumbs in: {self.search_dir}")
        self.scan_files()
        print(f"Found {len(self.breadcrumbs['files_found'])} files with breadcrumbs")
        
        print("Extracting connections...")
        self.extract_connections()
        
        print("Creating timeline...")
        self.create_timeline()
        
        print("Generating summary...")
        self.generate_summary()
        
        print("Saving results...")
        self.save_results()

def main():
    parser = argparse.ArgumentParser(description='Collect consciousness field breadcrumbs from your files')
    parser.add_argument('directory', nargs='?', default='.', help='Directory to search (default: current directory)')
    parser.add_argument('-o', '--output', default='consciousness_breadcrumbs.json', help='Output file name')
    parser.add_argument('-p', '--patterns', nargs='+', help='Additional patterns to search for')
    
    args = parser.parse_args()
    
    collector = BreadcrumbCollector(args.directory, args.output)
    
    if args.patterns:
        collector.consciousness_patterns.extend(args.patterns)
    
    collector.collect()

if __name__ == "__main__":
    main()
