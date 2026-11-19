# Manuscript figure-version lineage audit

Audited 2026-10-29. Scope: all **22 nonlock DOCX files** across `method_manuscript/` and `archive/20261118_superseded/method_manuscript/`, including the undated manuscript, the selected 2026-09-09 source, review/revision derivatives, the 2026-09-10 native Word file, and two test derivatives. This is a bounded comparison of empirical embedded figures, document image references, and accepted-view captions; it does not compare the full reviewed prose.

**Result: all 22 files contain the same five empirical figures, byte-for-byte. All accepted-view Figure 1–5 captions are also identical after whitespace normalization. No file in this set supplies changed plotted numbers or a newer empirical figure version.**

The selected `Adaptive_Replay_Manuscript_2026_09_09.docx` therefore has the same plotted evidence as both the undated source and `Adaptive_Replay_Manuscript_2026_09_10_precise_native_word.docx`. This conclusion comes from hashes and caption content, not the date or “final”/“revision” wording in filenames.

## Key source files

| File | Full-file SHA-256 | Figure bytes / captions |
|---|---|---|
| `Adaptive_Replay_Manuscript.docx` | `fbaab13913e2ad79cb567bca593fd6d6b9fedf24fc3b81330ab83c270a526163` | All five identical |
| `Adaptive_Replay_Manuscript_2026_09_09.docx` | `20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7` | All five identical |
| `Adaptive_Replay_Manuscript_2026_09_10_precise_native_word.docx` | `47bd249f0946001eb2f046fb66b84434f340ff142f5d5d503831823df08c9766` | All five identical |

## Figure identities

| Figure | Embedded member | SHA-256 |
|---|---|---|
| 1 | `word/media/image1.png` | `de944beace604d00d4eac20afaa7afd13d7b30087e71dd0bb5fd98682027abc0` |
| 2 | `word/media/image2.png` | `933ef4f0d03d942501db57e5c63b807a66aac8cf902033bceb86c25f2d2697b4` |
| 3 | `word/media/image3.png` | `26b8bd338133d392a667e0d01597010f6e8850dd517f5ffcd9c347dde0d1ff59` |
| 4 | `word/media/image4.png` | `624368f75b65d0660a746a591a125f3f7b0cbfdd3983bfb1fde01ec4d00bc121` |
| 5 | `word/media/image5.png` | `0f5a3c45e568af53e900765d28f68da4d8a2adcb2a288ec609ae3af56fe7a9e5` |

Every file has exactly five media assets, no additional numerical figure assets, and no native Word chart parts. All five are referenced by document images. Caption identities were checked in accepted view by excluding deleted/moved-from text and retaining insertions. The JSON records image references and complete normalized captions for every file. Archived files are included in the audit through the source-path list in `audit_manuscript_versions.py`.

## Complete file inventory

| File | Five figures byte-identical | Five captions identical |
|---|---|---|
| `Adaptive_Replay_Manuscript.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_PI_review_tracked_changes_comments.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_constructive_revision.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_constructive_revision_complete.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_constructive_revision_final.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_constructive_revision_full_comments.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_constructive_revision_full_comments_v2.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_constructive_revision_real_edits.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_constructive_revision_targeted_final.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_constructive_revision_targeted_green.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_constructive_revision_targeted_yellow.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_constructive_revision_v3.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_detailed_new_changes_green.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_new_targeted_review_green.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_precise_new_changes_green.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_precise_new_changes_green_fixed.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_precise_new_changes_green_wordonly.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_09_precise_new_changes_green_wordopen.docx` | Yes | Yes |
| `Adaptive_Replay_Manuscript_2026_09_10_precise_native_word.docx` | Yes | Yes |
| `test_no_new_comments.docx` | Yes | Yes |
| `test_remove_new_revs.docx` | Yes | Yes |

## Implications for the slides

- Keeping the 2026-09-09 manuscript as the figure source does not omit a different empirical figure version contained in these local derivatives.
- The current source discrepancies—Figure 4 versus Figure 5 percentage pairs, Figure 3 model/protocol identity, and the Figure 4 historical-metric caption conflict—are not resolved by choosing the differently dated or differently named manuscript files. The same empirical figures/captions recur throughout.
- These files are alternate document versions of the same plotted evidence; their names do not establish independent experiments or updated data.
- This audit does not establish which prose edits were approved, compare every body-text numerical claim, or recover raw prediction arrays, executed configurations, seeds, and split manifests. Those remain separate provenance questions.

Machine-readable record: `manuscript_version_figure_lineage.json`. Reproduction script: `audit_manuscript_versions.py`. The source DOCX files were read only; no manuscript or deck was changed.
